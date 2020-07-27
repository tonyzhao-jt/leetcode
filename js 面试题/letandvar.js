

// var and let
// var 变量提升
var a = 99;            // 全局变量a
f();                   // f是函数，虽然定义在调用的后面，但是函数声明会提升到作用域的顶部。 
console.log(a);        // a=>99,  此时是全局变量的a
function f() {
  console.log(a);      // 当前的a变量是下面变量a声明提升后，默认值undefined
  var a = 10;
  console.log(a);      // a => 10
}

// {} 限制不了 var 的范围。 let 可以声明块级作用域的变量

{ 
    var i = 9;
} 
console.log(i);  // 9


{ 
    let i = 9;     // i变量只在 花括号内有效！！！
} 
console.log(i);

// let 非常适合 for 循环内部的块级作用域
// 用 var 的话执行代码的时候同步循环已经执行完成

// let 不存在变量提升和重复声明
