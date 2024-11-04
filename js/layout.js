function adjustSizeGen() {
    var smallScreen = navigator.userAgent.toLowerCase().match(/(iphone|ipod)/);

    var gameRegion = $("#game-region"),
        tds = $('.board td'),
        board = $('.go-board'),
        gameHeader = $('header.game-ult'),
        gameInfo = $('#game-info'),
        mainButs = $('#main-but-group'),
        otherButs = $('#other-but-group');

    return function () {
        var avaih = window.innerHeight,
            avaiw = window.innerWidth,
            h = Math.max(avaih - 7, avaih * 0.98),
            w = Math.max(avaiw - 7, avaih * 0.98),
            vspace = Math.min(h - 100, w),  // Adjusted for a smaller board
            hspace = Math.min(w - 220, h - 40),  // Adjusted for a smaller board
            hsize;

        if (smallScreen) {
            if (avaih > avaiw) {
                vspace = avaiw;
                hspace = 0;
            } else {
                hspace = avaih - 40;
                vspace = 0;
            }
        }

        if (vspace > hspace) {
            hsize = Math.min(~~((vspace - 15) / 10 / 2), ~~((avaiw - 22) / 10 / 2));
            gameRegion.css({
                'padding': hsize + 6,
                'margin-left': -((2 * hsize + 1) * 10 - 2) / 2,
                'padding-top': 80 + hsize,
                'padding-bottom': 50 + hsize,
                'margin-top': -(10 * hsize + 60)
            });
            tds.css('padding', hsize);
            board.css({
                'top': 80,
                'bottom': 50,
                'left': 6,
                'right': 6
            });
            gameHeader.css('line-height', 60 + 'px');
            gameInfo.css({
                'top': 15,
                'width': ((2 * hsize + 1) * 10 + 12) / 2 - 100
            });
            mainButs.css({
                'top': 6,
                'right': hsize * 10 - 50,
                'width': 160
            });
            otherButs.css({
                'bottom': 6,
                'right': hsize * 10 - 50,
                'width': 160
            });
        } else {
            hsize = ~~((hspace - 15) / 10 / 2);
            gameRegion.css({
                'padding': hsize + 6,
                'margin-left': -((2 * hsize + 1) * 10 + 200) / 2,
                'padding-left': 120 + hsize,
                'padding-right': 120 + hsize,
                'padding-top': 30 + hsize,
                'margin-top': -(hsize * 10 + 20)
            });
            tds.css('padding', hsize);
            board.css({
                'top': 20,
                'bottom': 18,
                'left': 120,
                'right': 120
            });
            gameHeader.css('line-height', 30 + hsize + 'px');
            gameInfo.css({
                'left': 10,
                'top': 30 + hsize,
                'width': 120 + 6 - 45 - hsize / 2
            });
            mainButs.css({
                'top': 12 + hsize,
                'right': 9,
                'width': 160
            });
            otherButs.css({
                'bottom': 6 + hsize,
                'right': 6,
                'width': 160
            });
        }

    };
}
