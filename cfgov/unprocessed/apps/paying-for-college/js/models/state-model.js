/**
 * This file contains the model for the application state - that is, an Object
 * which tracks the current app state and allows the views to update based on
 * state.
*/
import { getProgramInfo, getSchoolValue } from '../dispatchers/get-model-values.js';
import { recalculateFinancials } from '../dispatchers/update-models.js';
import { updateFinancialViewAndFinancialCharts, updateNavigationView, updateSchoolItems, updateStateInDom, updateUrlQueryString } from '../dispatchers/update-view.js';
import { bindEvent } from '../../../../js/modules/util/dom-events';

const stateModel = {
  stateDomElem: null,
  values: {
    activeSection: false,
    advancedPastSearch: false,
    constantsLoaded: false,
    costsQuestion: false,
    gotStarted: false,
    gradMeterCohort: 'cohortRankByHighestDegree',
    gradMeterCohortName: 'U.S.',
    pid: false,
    programHousing: 'not-selected',
    programLength: 'not-selected',
    programLevel: 'not-selected',
    programRate: 'not-selected',
    programType: 'not-selected',
    programStudentType: 'not-selected',
    repayMeterCohort: 'cohortRankByHighestDegree',
    repayMeterCohortName: 'U.S.',
    salaryAvailable: "no",
    schoolSelected: "none"
  },
  textVersions: {
    programType: {
      certificate: 'certificate',
      associates: 'Associates\'s Degree',
      bachelors: 'Bachelor\'s Degree',
      graduate: 'Graduate\'s Degree'
    },
    programLength: {
      1: '1 year',
      2: '2 years',
      3: '3 years',
      4: '4 years',
      5: '5 years',
      6: '6 years'
    },
    programHousing: {
      onCampus: 'On campus',
      offCampus: 'Off campus (you will pay rent/mortgage)',
      withFamily: 'With family (you will not pay rent/mortgage)'
    },
    programRate: {
      inState: 'In-state',
      outOfState: 'Out of state',
      inDistrict: 'In district'
    }
  },
  sectionOrder: [
    'school-info',
    'costs',
    'grants-scholarships',
    'work-study',
    'federal-loans',
    'school-loans',
    'other-resources',
    'loan-counseling',
    'make-a-plan',
    'max-debt-guideline',
    'cost-of-borrowing',
    'affording-your-loans',
    'school-results',
    'summary',
    'action-plan',
    'save-and-finish'
  ],

  /**
   * pushStateToHistory - Push current application state to window.history
   */
  pushStateToHistory: () => {
    const historyState = {
      activeSection: stateModel.values.activeSection
    };
    window.history.pushState( historyState, null, window.location.search );
  },

  /**
   * replaceStateInHistory - Replace current application state in window.history
   * @param {string} queryString - The queryString to put in the history object
   */
  replaceStateInHistory: queryString => {
    const historyState = {
      activeSection: stateModel.values.activeSection
    };
    if ( typeof queryString === 'undefined' ) queryString = window.location.search;
    window.history.replaceState( historyState, null, queryString );
  },

  /**
   * setValue - Public method to update model values
   * @param {string} name - the name of the property to update
   * @param {string|number|boolean} value - the value to be assigned
   */
  setValue: function( name, value ) {
    // In case this method gets used to update activeSection...
    if ( name === 'activeSection' ) {
      stateModel.setActiveSection( value );
    }
    stateModel.values[name] = value;
    updateStateInDom( name, value );

    stateModel._updateApplicationState( name );
    console.log( 'setValue: ', name, value );
  },

  /**
   * setActiveSection - Method to update the app's active section
   * @param {*} value - the value to be assigned
   * @param {Boolean} popState - true if the update is the result of a popState event
   */
  setActiveSection: function( value, popState ) {
    updateStateInDom( 'activeSection', value );
    stateModel.setValue( 'save-for-later', false );
    stateModel.values.activeSection = value;
    if ( popState !== true ) {
      stateModel.pushStateToHistory();
    }
    updateNavigationView();
  },

  /**
   * Check whether required fields are selected
   */
  _checkRequiredFields: () => {
    // Only change error state if the user has advanced or attempts to advance
    // past the search page.
    if ( !advancedPastSearch ) {
      const smv = stateModel.values;
      const control = getSchoolValue( 'control' );

      const requiredErrors = {
        schoolHasBeenSelected: ( smv.schoolSelected === 'none' ),
        housingSelected: smv.programHousing === 'not-selected',
        lengthSelected: smv.programLength === 'not-selected',
        typeSelected: smv.programType === 'not-selected',
        dependencySelected: smv.programType === 'undergrad' && smv.dependencySelected === 'not-selected',
        rateSelected: smv.programRate === 'not-selected' && control === 'Public'
      };

      // Change values to "required" which triggers error notification CSS rules
      for ( let key in requiredErrors ) {
        if ( requiredErrors[key] === true ) {
          stateModel.values[key] = 'required';
          updateStateInDom( key, 'required' );
        }
      }
    }
  },

  /**
   * set the salaryAvailable property based on other values
   */
  _setSalaryAvailable: () => {
    let available = "yes";
    const smv = stateModel.values
    if ( smv.programLevel === 'graduate' && smv.pid === false ) {
      available = "no";
    }
    stateModel.values.salaryAvailable = available;
    updateStateInDom( 'salaryAvailable', available );
    console.log( 'salaryAvailable set to "' + available + '".' );
  },

  /**
   * set programLevel property based on programType
   */
   _setProgramLevel: () => {
    const programType = stateModel.values.programType;
    let programLevel = 'undergrad';
    if ( programType === 'graduate' ) {
      programLevel = 'graduate';
    }

    stateModel.values.programLevel = programLevel;
    updateStateInDom( 'programLevel', programLevel );
   },

  /**
   * update the application state based on the 'property' parameter.
   * @param {string} property - What property to update based on
   */
  _updateApplicationState: ( property ) => {
    const urlParams = [ 'pid', 'programHousing','programType', 'programLength',
      'programRate', 'programStudentType', 'costsQuestion', 'expensesRegion',
      'impactOffer', 'impactLoans', 'utmSource', 'utm_medium', 'utm_campaign' ];

    const finUpdate = [ 'programType', 'programRate', 'programStudentType',
      'programLength', 'programHousing' ];

    // Properties which require a URL querystring update:
    if ( urlParams.indexOf( property ) > -1 ) {
      updateUrlQueryString();
    }

    // Properties which require a financialModel and financialView update:
    if ( finUpdate.indexOf( property ) > -1 ) {
      recalculateFinancials();
      updateFinancialViewAndFinancialCharts();
    }

    if ( stateModel.textVersions.hasOwnProperty( property ) ) {
      const value = stateModel.values[property];
      const key = property + 'Text';
      stateModel.values[key] = stateModel.textVersions[property][value];
      updateSchoolItems();
    }

    // When the meter buttons are clicked, updateSchoolItems
    if ( property.indexOf( 'MeterThird' ) > 0 ) {
      updateSchoolItems();
    }

    // Update state values which are based on other values
    stateModel._setProgramLevel();
    stateModel._setSalaryAvailable();
    stateModel._checkRequiredFields();
  }

};

export {
  stateModel
};
