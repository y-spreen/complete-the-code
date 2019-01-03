function main() {
    let b = $(".body");

    let h = b.height();
    let w = b.width();
    b.css("max-width", h + "px");
    b.css("max-height", w + "px");

    draw();
}

function draw() {
    var c = $("canvas")[0];
    var ctx = c.getContext("2d");
    ctx.fillStyle = "white";
    ctx.fillRect(0, 0, 100, 100);
    ctx.fillStyle = "black";

    for (let i = 0; i < 1000; i += 10) {
        ctx.fillStyle = "black";
        if (Math.random() >= 0.5)
            ctx.fillRect(i % 100, Math.floor(i / 100) * 10, 10, 10);
    }

    setTimeout(draw, 2000);
}

$(main);