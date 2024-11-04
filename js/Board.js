// Board.js
function Place(r, c, board) {
    // Create a cell on the board
    var elm = this.elm = document.createElement("div");
    elm.className = "go-place";
    var s = elm.style;
    s.top = r / 10 * 100 + '%';
    s.left = c / 10 * 100 + '%';
    s.right = 100 - (c + 1) / 10 * 100 + '%';
    s.bottom = 100 - (r + 1) / 10 * 100 + '%';
    s.position = 'absolute';
    
    var inner = document.createElement("div");
    inner.className = "go";
    elm.appendChild(inner);

    // Add touch events for mobile devices
    if ("ontouchstart" in window) {
        var moved = false;
        elm.ontouchstart = function(e) {
            moved = false;
            return false;
        };
        elm.ontouchmove = function(e) {
            moved = true;
            return false;
        };
        elm.ontouchend = function(e) {
            if (!moved) {
                board.clicked(r, c);
            }
            moved = false;
            return false;
        };
    }

    elm.onclick = function() {
        board.clicked(r, c);
    };

    this.elm = $(elm);
    this.isSet = false;
}

Place.prototype.set = function(color) {
    this.elm.addClass("set").addClass(color).removeClass("warning");
    this.isSet = true;
};

Place.prototype.unset = function() {
    this.elm.removeClass("black").removeClass("white").removeClass("set").removeClass("last-move");
    this.isSet = false;
};

Place.prototype.highlight = function() {
    this.elm.addClass("last-move");
};

Place.prototype.warns = function() {
    this.elm.addClass("warning");
};

Place.prototype.unwarns = function() {
    this.elm.removeClass("warning");
};

var Board = function(boardElm, backgroundElm) {
    var frag = document.createDocumentFragment();

    // Create a 10x10 board grid
    for (var i = 0; i < 10; i++) {
        var row = document.createElement("tr");
        for (var j = 0; j < 10; j++) {
            row.appendChild(document.createElement("td"));
        }
        frag.appendChild(row);
    }
    backgroundElm.append(frag);

    var self = this;
    var clickable = true,
        places = [],
        map = [],
        numToColor = ["black", "white"],
        colorToNum = (function() {
            var obj = {};
            numToColor.forEach(function(elm, ind) {
                obj[elm] = ind;
            });
            return obj;
        })(),
        moves = [
            [1, 0],
            [0, 1],
            [1, 1],
            [1, -1]
        ],
        setNum = 0;

    frag = document.createDocumentFragment();

    for (var r = 0; r < 10; r++) {
        places.push([]);
        for (var c = 0; c < 10; c++) {
            places[r].push(new Place(r, c, this));
            frag.appendChild(places[r][c].elm[0]);
        }
    }
    for (var i = 0; i < 10; i++) {
        for (var j = 0; j < 10; j++) {
            places[i][j].elm.addClass("go-smalldot");
        }
    }
    // Center points for 10x10 board
    [[5, 5], [2, 2], [2, 7], [7, 2], [7, 7]].forEach(function(e) {
        places[e[0]][e[1]].elm.removeClass("go-smalldot").addClass("go-darkdot");
    });

    boardElm.append(frag);

    (function() {
        for (var i = 0; i < 2; i++) {
            var tmp = [];
            for (var j = 0; j < 4; j++) {
                var tmpp = [];
                for (var k = 0; k < 10; k++) {
                    var tmpr = [];
                    for (var l = 0; l < 10; l++) {
                        tmpr.push(1);
                    }
                    tmpp.push(tmpr);
                }
                tmp.push(tmpp);
            }
            map.push(tmp);
        }
    })();

    this.setClickable = function(yes, color) {
        clickable = yes;
        if (yes) {
            boardElm.addClass("playing");
        } else {
            boardElm.removeClass("playing");
        }
        if (color) {
            boardElm.removeClass("black").removeClass("white").addClass(color);
        }
    };

    this.setGo = function(r, c, color) {
        places[r][c].set(color);
        setNum++;
    };

    this.unsetGo = function(r, c) {
        places[r][c].unset();
        this.updateMap(r, c);
        setNum--;
    };

    this.highlight = function(r, c) {
        this.unHighlight();
        places[r][c].highlight();
    };

    this.unHighlight = function() {
        $(".last-move").removeClass("last-move");
    };

    this.winChange = function(r, c, color) {
        boardElm.find(".warning").removeClass("warning");
        var num = colorToNum[color],
            dir;
        for (var i = 0; i < 4; i++) {
            if (map[num][i][r][c] >= 5) {
                dir = i;
                break;
            }
        }
        $(".go-place").css("opacity", 0.5);
        for (var i = -1; i < 2; i += 2) {
            var rr = r, cc = c;
            do {
                places[rr][cc].elm.css("opacity", 1);
                rr += moves[dir][0] * i;
                cc += moves[dir][1] * i;
            } while (rr >= 0 && rr < 10 && cc >= 0 && cc < 10 && map[num][dir][rr][cc] === -num);
        }
    };

    this.isSet = function(r, c) {
        return places[r][c].isSet;
    };

    this.getGameResult = function(r, c, lastColor) {
        var n = colorToNum[lastColor];
        if (map[n].some(function(e) {
            return e[r][c] > 4;
        })) {
            return "win";
        }
        if (setNum === 100) {
            return "draw";
        }
        return false;
    };

    this.init = function() {
        boardElm.find(".warning").removeClass("warning");
        boardElm.find(".go-place").css("opacity", "");
        this.unHighlight();
        setNum = 0;
        map.forEach(function(color) {
            color.forEach(function(direction) {
                direction.forEach(function(row) {
                    row.forEach(function(column, ind) {
                        row[ind] = 1;
                    });
                });
            });
        });
        places.forEach(function(row) {
            row.forEach(function(p) {
                p.unset();
            });
        });
    };

    var warnings = [false, false];

    this.setWarning = function(num, shouldWarn) {
        warnings[num] = !!shouldWarn;
    };

    function updateWarning(r, c, num, dir) {
        if (warnings[num]) {
            if (map[num][dir][r][c] > 4) {
                places[r][c].warns();
            } else {
                places[r][c].unwarns();
            }
        }
    }

    window.m = map;
    this.updateMap = function(r, c, color) {
        var remove = false,
            num = colorToNum[color];
        if (num === undefined) {
            remove = true;
        }
        _updateMap(r, c, num, remove);
    };

    function _updateMap(r, c, num, remove) {
        if (remove) {
            for (num = 0; num < 2; num++) {
                for (var i = 0; i < 4; i++) {
                    map[num][i][r][c] = 1;
                    updateWarning(r, c, num, i);
                    for (var coe = -1; coe < 2; coe += 2) {
                        var x = r, y = c, len = 0;
                        do {
                            x += moves[i][0] * coe;
                            y += moves[i][1] * coe;
                            len++;
                        } while (x >= 0 && y >= 0 && x < 10 && y < 10 && map[num][i][x][y] === -num);
                        if (x >= 0 && y >= 0 && x < 10 && y < 10 && map[num][i][x][y] > 0) {
                            map[num][i][x][y] = len;
                            updateWarning(x, y, num, i);
                            map[num][i][r][c] += len - 1;
                            updateWarning(r, c, num, i);
                            var cont = 0, mx = x + moves[i][0] * coe, my = y + moves[i][1] * coe;
                            while (mx >= 0 && my >= 0 && mx < 10 && my < 10 && map[num][i][mx][my] === -num) {
                                cont++;
                                mx += moves[i][0] * coe;
                                my += moves[i][1] * coe;
                            }
                            map[num][i][x][y] += cont;
                            updateWarning(x, y, num, i);
                        } else {
                            map[num][i][r][c] += len - 1;
                            updateWarning(r, c, num, i);
                        }
                    }
                }
            }
        } else {
            for (var i = 0; i < 4; i++) for (var coe = -1; coe < 2; coe += 2) {
                var x = r, y = c;
                do {
                    x += moves[i][0] * coe;
                    y += moves[i][1] * coe;
                } while (x >= 0 && y >= 0 && x < 10 && y < 10 && map[num][i][x][y] === -num);
                if (x >= 0 && y >= 0 && x < 10 && y < 10 && map[num][i][x][y] > 0) {
                    map[num][i][x][y] = map[num][i][r][c] + 1;
                    var cont = 0, mx = x + moves[i][0] * coe, my = y + moves[i][1] * coe;
                    while (mx >= 0 && my >= 0 && mx < 10 && my < 10 && map[num][i][mx][my] === -num) {
                        cont++;
                        mx += moves[i][0] * coe;
                        my += moves[i][1] * coe;
                    }
                    map[num][i][x][y] += cont;
                    updateWarning(x, y, num, i);
                }
                x = r;
                y = c;
                do {
                    x += moves[i][0] * coe;
                    y += moves[i][1] * coe;
                } while (x >= 0 && y >= 0 && x < 10 && y < 10 && map[1 - num][i][x][y] == num - 1);
            }
            for (var i = 0; i < 2; i++) for (var j = 0; j < 4; j++) {
                map[i][j][r][c] = -num;
                updateWarning(r, c, num, i);
            }
        }
    }
};
