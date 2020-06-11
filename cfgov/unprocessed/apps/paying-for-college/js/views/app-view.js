

/* This file handles view items which apply only to the "state" of the
application, and are otherwise inappropriate for the
other views. */

const appView = {
  _didThisHelpBtns: null,

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
    console.log( event.target.value );
  },

  /**
   * Initialize the View
   */
   init: () => {
    appView._didThisHelpBtns = document.querySelectorAll( '#save_did-it-help button, #save_understand-loans button' );
   }
};

export {
  appView
}