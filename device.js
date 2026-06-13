// device.js - Juster Responsive Controller
const DeviceManager = {
    isMobile: function() {
        return window.innerWidth <= 768; // Standard breakpoint
    },

    getSignal: function() {
        if (this.isMobile()) {
            return "SIGNAL_COMPACT"; // Optimized for your realme
        } else {
            return "SIGNAL_WIDE";    // Optimized for tablets/desktop
        }
    },

    init: function() {
        const signal = this.getSignal();
        console.log("BlueBixt Device Signal:", signal);
        
        // You can add logic here to trigger different styles 
        // or functionality based on the signal
        document.body.classList.add(signal);
    }
};

DeviceManager.init();
  
