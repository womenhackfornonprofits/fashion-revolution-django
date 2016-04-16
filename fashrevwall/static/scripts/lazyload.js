document.addEventListener('DOMContentLoaded', function(event) {


    (function lazyload() {

        function isInRange(el) {
            var WindowTop = window.scrollY - (document.clientTop || 0);
            var WindowBottom = WindowTop + window.innerHeight;
            var elTop = getTop(el);
            var elBottom = elTop + el.offsetHeight;

            function getTop(element) {
                var top = 0;
                while (element) {
                    top += element.offsetTop;
                    element = element.offsetParent;
                }
                return top;
            }

            var padding = 100;
            return elTop < WindowBottom + padding && elBottom > WindowTop - padding;
        }

        function loadImages(els) {
            for (var i = 0; i < els.length; i++) {
                if (isInRange(els[i])) {
                    els[i].style.backgroundImage = els[i].getAttribute('data-image');
                }
            }
        }

        var throttled = false;

        document.addEventListener('scroll', function(ev) {
            if (throttled) { return; }
            loadImages(document.getElementsByClassName('js-lazyload'));

            throttled = true;

            setTimeout(function() {
                throttled = false;
            }, 100);

        });


        // Then load those in view
        loadImages(document.getElementsByClassName('js-lazyload'));

    })();

});