// js this 的 四种绑定规则
/*
    默认绑定
    隐式绑定
    显式绑定
    new 绑定
*/

// 默认绑定
function foo() {
    console.log(this.a)   // 输出 a
  }
  
var a = 2;  //  变量声明到全局对象中

foo();

// 隐式绑定
// 调用位置存在上下文对象

function foo() {
console.log(this.a);
}

let obj1 = {
a: 1,
foo,
};

let obj2 = {
a: 2,
foo,
}

obj1.foo();   // 输出 1
obj2.foo();   // 输出 2

// 显示绑定
// 用 function prototype 中的 call apply bind
function foo() {
    console.log(this.a);  // 输出 1
    bar.apply({a: 2}, arguments);
  }
  
  function bar(b) {
    console.log(this.a + b);  // 输出 5
  }
  
  var a = 1;
  foo(3);

// new 绑定
