## 基础数据类型
- undefined
  - var 声明变量但为初始化
- null
  - 空对象指针
- boolean
  - true and false
- string
  - .toString()
- number    
  - 0 和 NaN（not a number）
  - 任何设计 NaN 的操作都会返回 NaN， NaN 和任何数值都不相等
- object


## call(), apply(), bind()
- 都是重定义 this 这个对象的
- bind 返回一个新的函数，调用才会执行
- call 的参数直接放进去，参数之间用逗号分割
- apply 放入数组
- bind 和 call 一样，除了返回是函数

# 实例原型，构造函数和对象
构造函数 --- prototype ---> 实例原型
实例原型 --- constructor  ---> 构造函数
类型实例 ---> _proto_ -> 实例原型
- 原型链条，实例原型是另外一个构造函数的实例
- 会向上读取

# JS 回收和闭包
- 全局变量不会被回收
- 局部变量会被回收
- 只要被另外一个作用域引用就不会被回收

```js
function aaa() {  
    var a = 1;  
    return function(){
    alert(a++)
    };  
}         
var fun = aaa();  
fun();// 1 执行后 a++，，然后a还在~  
fun();// 2   
fun = null;//a被回收！！
```

# cors
```js
app.all('*', function(req, res, next){
    res.header()
    res.header()
    next()
})
```



