// 箭头函数

/*
    函数体内的 this 对象就是定义时所在的对象
    不可以当作构造函数，不能使用 new
    不可以使用 yield 作为 generator
*/


// 不适用场合
// 定义对象的方法

const cat = {
    lives: 9,
    jumps: () => {
    this.lives--;
    }
}

// 2
var button = document.getElementById('press');
button.addEventListener('click', () => {
 this.classList.toggle('on');
});