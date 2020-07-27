// 对象的深克隆和浅克隆
let a = {},
    b = '0',
    c = 0;
a[b] = 'first'
a[c] = 'second'
console.log(a[b]);
// second

// 堆，基本类型不会存在堆
// 属性名不能重复

let a = {},
    b = Symbol('0'), // 创建唯一值
    c = Symbol('1');
a[b] = 'first'
a[c] = 'second'
console.log(a[b]);
// 自己实现 sumbol
// first
"object object"

// 对象和数组的区别

var test = (function (i){
    return function(){
        alert(i *= 2)
    }
})(2);
test(5);

// '4'
