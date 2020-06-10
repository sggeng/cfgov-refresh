/**
 * The file interfaces between our application and the studentDebtCalculator package
 */

import studentDebtCalculator from 'student-debt-calc';
import { calcDebtAtGrad, calcMonthlyPayment } from './debt-utils.js';
import { getConstantsValue, getFinancialValue, getStateValue } from '../dispatchers/get-model-values.js';
import { constantsModel } from '../models/constants-model.js';
import { financialModel } from '../models/financial-model.js';
import { updateFinancial, updateFinancialsFromSchool } from '../dispatchers/update-models.js';

// Please excuse some uses of underscore for code/HTML property clarity!
/* eslint camelcase: ["error", {properties: "never"}] */




function debtCalculator() {
  const fedLoans = [ 'directSub', 'directUnsub', 'gradPlus', 'parentPlus' ];
  const otherLoans = [ 'state', 'institutional', 'nonprofit', 'privateLoan1' ];
  const allLoans = fedLoans.concat( otherLoans );
  let fin = financialModel.values;
  let debts = {
    totalAtGrad: 0,
    tenYearTotal: 0,
    tenYearMonthly: 0,
    tenYearInterest: 0,
    twentyFiveYearTotal: 0,
    twentyFiveYearMonthly: 0,
    twentyFiveYearInterest: 0,
  };

  // Find federal debts at graduation
  fedLoans.forEach( ( key ) => {
    // DIRECT Subsidized loans are special
    let val = 0;
    if ( key === 'directSub' ) {
      val = fin[ 'fedLoan_' + key ] * fin.other_programLength;
    } else {
      val = calcDebtAtGrad( fin[ 'fedLoan_' + key ],
        fin[ 'rate_' + key ], fin.other_programLength, 6 );
    }

    // if ( val === NaN ) {
    //   val = 0;
    // }
    debts[key] = val;

  } );

  // calculate debts of other loans

  otherLoans.forEach( ( key ) => {
    let val = calcDebtAtGrad(
        fin[ 'loan_' + key],
        fin[ 'rate_' + key ],
        fin.other_programLength,
        0
      );

    if ( val === NaN ) {
      val = 0;
    }
    debts[key] = val;

  } );

  // 10 year term calculations.
  allLoans.forEach( ( key ) => {
    debts.totalAtGrad += debts[key];
    let tenYearMonthly = calcMonthlyPayment(
        debts[key],
        fin[ 'rate_' + key ],
        10
      )

    if ( tenYearMonthly === NaN ) {
      tenYearMonthly = 0;
    }
    // debts[ key + '_tenYearMonthly' ] = tenYearMonthly;
    // debts[ key + '_tenYearTotal' ] = tenYearMonthly * 120;
    // debts[ key + '_tenYearInterest' ] = (tenYearMonthly * 120 ) - debts[key];
    debts.tenYearMonthly += tenYearMonthly;
    debts.tenYearTotal += ( tenYearMonthly * 120 );

    // 25 year term calculations
    let twentyFiveYearMonthly = calcMonthlyPayment(
        debts[key],
        fin[ 'rate_' + key ],
        10
      )

    if ( twentyFiveYearMonthly === NaN ) {
      twentyFiveYearMonthly = 0;
    }
    // debts[ key + '_twentyFiveYearMonthly' ] = twentyFiveYearMonthly;
    // debts[ key + '_twentyFiveYearTotal' ] = twentyFiveYearMonthly * 300;
    // debts[ key + '_twentyFiveYearInterest' ] = ( twentyFiveYearMonthly * 300 ) - debts[key];
    debts.twentyFiveYearMonthly += twentyFiveYearMonthly;
    debts.twentyFiveYearTotal += ( twentyFiveYearMonthly * 300 );

  } );

  debts.tenYearInterest = debts.tenYearTotal - debts.totalAtGrad;
  debts.twentyFiveYearInterest = debts.twentyFiveYearTotal - debts.totalAtGrad;
  debts.repayHours = debts.tenYearMonthly / 15;
  debts.repayWorkWeeks = debts.repayHours / 40;

  // TODO: Differentiate grads versus undergrads

  // TODO: Apply the changing-over-time DIRECT maxes to DIRECT borrowing

  // TODO: Toggle for parentPlus debt

  for ( let key in debts ) {
    fin[ 'debt_' + key] = debts[key];
  }

}


export {
  debtCalculator
};
