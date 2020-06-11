/* This file handles view items which apply only to the "state" of the
application, and are otherwise inappropriate for the
other views. */

import { bindEvent } from '../../../../js/modules/util/dom-events';
import { closest } from '../../../../js/modules/util/dom-traverse';

const appView = {
  _didThisHelpBtns: null,
  _finishLink: '',

  /**
   * Listeners for buttons
   */
  _addButtonListeners: function() {
    appView._didThisHelpBtns.forEach( elem => {
      const events = {
        click: this._handleDidThisHelpBtns
      };
      bindEvent( elem, events );
    } );
  },

  /**
   * Handle the click of buttons on final page
   * @param {Object} event - Click event object
   */
  _handleDidThisHelpBtns: event => {
    const button = event.target;
    const parent = closest( button, '.m-btn-group' );
    button.classList.remove( 'a-btn__disabled')
    parent.querySelectorAll( 'button:not( [value="' + button.value + '"]' )
      .forEach( elem => {
        elem.classList.add( 'a-btn__disabled' );
      } );
      
    console.log( event.target.value );
  },

  /**
   * Update the link on the save and finish page with the current url
   */
  _updateSaveLink: () => {
    appView._finishLink.value = window.location.href;
  },

  /**
   * Public method for updating this view
   */
  updateView: () => {
    appView._updateSaveLink();
  },

  /**
   * Initialize the View
   */
   init: () => {
    appView._didThisHelpBtns = document.querySelectorAll( '#save_did-it-help button, #save_understand-loans button' );
    appView._finishLink = document.querySelector( '#finish_link' );

    appView._addButtonListeners();
   }
};

export {
  appView
}