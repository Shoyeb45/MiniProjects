let boxes = document.querySelectorAll(".box");
let resetBtn = document.querySelector("#resetBtn");

let turnO = false;
// Winning pattern
const winPattern = [
    [0, 1, 2],
    [0, 3, 6],
    [0, 4, 8],
    [1, 4, 7],
    [2, 5, 8],
    [2, 4, 6],
    [3, 4, 5],
    [6, 7, 8]
];

boxes.forEach((box) => {
    box.addEventListener("click", () => {
        // condition for turns
        if(turnO) {
            turnO = false;
            box.innerText = "O";
        } else {
            turnO = true;
            box.innerText = "X";
        }
        box.disabled = true;
        checkWinner();
    })
})


// function for checking the winning pattern
const checkWinner = () => {
    for(let pattern of winPattern) {
        let valPos1 = boxes[pattern[0]].innerText;
        let valPos2 = boxes[pattern[1]].innerText;
        let valPos3 = boxes[pattern[2]].innerText;

        if(valPos1 != "" && valPos2 != "" && valPos3 != "") {
            if(valPos1 === valPos2 && valPos2 === valPos3) {
                alert("Winner");
            }
        }
    }
}