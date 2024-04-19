const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d")
const WIDTH = 600
const HEIGHT = 600

let T = 12;

// ctx.clearRect(10, 10, 50, 50)

ctx.fillStyle = "rgb(194, 178, 128)";
ctx.shadowBlur = 9;
ctx.shadowColor = "rgb(190, 150, 12)";



// function drawSand(x, y) {

//     ctx.fillRect(x, y, 8, 8);
//     ctx.fill();

// }

// let x = [0,0]

// canvas.addEventListener('mousedown', function(e){ 
//     drawSand(e.x, e.y)
//     console.log(e.x, e.y)
// })



// let y = [0,0]
// let v = [0,0]
// setInterval(function(){
//     ctx.clearRect(0, 0, canvas.clientWidth, canvas.clientHeight)
//     for (let i = 0; i< 2; i++){
//         y[i] = (y[i] + v[i]*(1000/60))
//         v[i] = (v[i] + 0.001*(1000/60))
//         if (y[i] > 592){
//             drawSand(50,592)
//         }
//         else{
//             drawSand(50,50+y[i])
//             y[i]+=1
//         }
//     }


    
    
// }, 1000/60)


class Grid {
    constructor() {
        this.grid = Array.from({ length: WIDTH * 2 }, () => Array(HEIGHT + T).fill(0));
        this.position = [];
    }

    addSand(pointX, pointY) {
        if (pointX >= 0 && pointX <= WIDTH && pointY >= 0 && pointY <= HEIGHT) {
            if (this.grid[pointX][pointY] === 0){
                this.grid[pointX][pointY] = 1;
                this.position.push([pointX, pointY])};
            if (this.grid[pointX+T][pointY+T] === 0) {
                this.grid[pointX+T][pointY+T] = 1;
                this.position.push([pointX+T, pointY+T])}
            if (this.grid[pointX][pointY-T] === 0) {
                this.grid[pointX][pointY-T] = 1;
                this.position.push([pointX, pointY-T])}
            
        }
    }

    updatePosition() {
        for (let i = this.position.length - 1; i >= 0; i--) {
            let points = this.position[i];
            let [x, y] = points;

            if (y >= HEIGHT - T) {
                continue; // Skip if sand is at the bottom
            }

            if (x < 0 || x > 600-T) {
                continue; // Skip if sand is at the bottom
            }

            if (this.grid[x][y + T] === 0 ) {
                this.grid[x][y] = 0;
                this.grid[x][y + T] = 1;
                points[1] += T;
            } else if (this.grid[x][y + T] === 1) {
                if ((this.grid[x + T] && this.grid[x + T][y + T] === 1) && (this.grid[x - T] && this.grid[x - T][y + T] === 1)) {
                    continue; // Skip if sand is blocked
                } else if ((!this.grid[x + T] || this.grid[x + T][y + T] === 1) && (!this.grid[x-T] ||  this.grid[x - T][y + T] === 0)) {
                    if ((x)>=T){

                        this.grid[x][y] = 0;
                        this.grid[x - T][y + T] = 1;
                        points[0] -= T;
                        points[1] += T;
                    }
                    else{continue}
                    

                } else if ((!this.grid[x + T] || this.grid[x + T][y + T] === 0) && (!this.grid[x - T] || this.grid[x - T][y + T] === 1)) {
                    this.grid[x][y] = 0;
                    this.grid[x + T][y + T] = 1;
                    points[0] += T;
                    points[1] += T;
                } else {
                    this.grid[x][y] = 0;
                    let a = Math.random() < 0.5 ? -1 : 1;
                    if (this.grid[x + a * T]) {
                        this.grid[x + a * T][y + T] = 1;
                    }
                    points[0] += a * T;
                    points[1] += T;
                }
            }
        }
    }

    draw(ctx) {
        
        this.position.forEach(points => {
            ctx.fillRect(points[0], points[1], T, T);
        });
    }
}




let sandbox = new Grid();



setInterval(function(){
    canvas.addEventListener("mousemove", function(event) {
        console.log(event.button)
        if (event.buttons === 1) {
            const rect = canvas.getBoundingClientRect();
            const scaleX = canvas.width / rect.width;
            const scaleY = canvas.height / rect.height;
            const mouseX = (event.clientX - rect.left) * scaleX;
            const mouseY = (event.clientY - rect.top) * scaleY;
            sandbox.addSand(Math.floor(mouseX / T) * T, Math.floor(mouseY / T) * T);
        }
    });


    ctx.clearRect(0, 0, canvas.clientWidth, canvas.clientHeight)
    sandbox.updatePosition();
    sandbox.draw(ctx);
    
}, 1000/40)


    // function animate() {
    //     if (!run) return;
    //     requestAnimationFrame(animate);

        // ctx.clearRect(0, 0, canvas.width, canvas.height);
        // sandbox.updatePosition();
        // sandbox.draw(ctx);
    // }



// Call the main function when the document is loaded
// document.addEventListener("DOMContentLoaded", main);



