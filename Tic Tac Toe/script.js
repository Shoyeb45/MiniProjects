// Accessing all necessary html elements
let boxes = document.querySelectorAll(".box");
let resetBtn = document.querySelector("#resetBtn");
let newGameBtn = document.querySelector("#newGameBtn");
let msg = document.querySelector("#msg");
let msgContainer = document.querySelector(".msgContainer");

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

// Event listener for clicking button
boxes.forEach((box) => {
    box.addEventListener("click", () => {
        // condition for turns
        if(turnO) {
            turnO = false;
            box.innerText = "O";
            box.style.color = "red";
        } else {
            turnO = true;
            box.innerText = "X";
            box.style.color = "aqua";
        }
        box.disabled = true;
        checkWinner();
    })
})

const resetGame = () => {
    turnO = true;
    enableBtn();
    msgContainer.classList.add("hide");
    count = 0;
}

// Function for disabling the button after winner is found
const disableBtn = () => {
    for (let box of boxes) {
        box.disabled = true;
    }
}

// Function for enabling the button after reset button is tapped
const enableBtn = () => {
    for (let box of boxes) {
        box.disabled = false;
        box.innerText = "";
    }
    count = 0;
}

// Function for checking the winner
const showWinner = (winner) => {
    msg.innerText = `Congratulation, the winner is ${winner}`;
    msgContainer.classList.remove("hide");
    disableBtn();
}

// function for checking the winning pattern
let count = 0;
const checkWinner = () => {
    for(let pattern of winPattern) {
        let valPos1 = boxes[pattern[0]].innerText;
        let valPos2 = boxes[pattern[1]].innerText;
        let valPos3 = boxes[pattern[2]].innerText;

        if(valPos1 != "" && valPos2 != "" && valPos3 != "") {
            if(valPos1 === valPos2 && valPos2 === valPos3) {
                showWinner(valPos1);
            }
        }
    }
    count++;
    if(count === 9) {
        msg.innerText = "Game is draw";
        msgContainer.classList.remove("hide");
        disableBtn();
    }
}

// Events for reset button and new game

newGameBtn.addEventListener("click", resetGame);
resetBtn.addEventListener("click", resetGame);