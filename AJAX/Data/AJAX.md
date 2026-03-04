# 1. AJAX 入门

## 1.1 什么是 AJAX?

AJAX 是异步的 JavaScript 和 XML（Asynchronous JavaScript And XML）。就是 XHLHttpRequest 对象和服务器通信。他可以使用JSON, XML, HTML，和 text 文本等格式发送和接受数据。AJAX 可以在不重新刷新页面的情况下与服务器通信，交换数据，或更新页面。



## 1.2 怎么使用AJAX

1. 先使用 axios 库，与服务器进行数据通信
   - 基于 XMLHttpRequest 封装、代码简单
   - Vue、React 项目中都会用到 axios
2. 再学习 XMLHttpRequest 对象的使用，了解 AJAX 的原理

## 1.3 axios 使用

**语法：**

1. 引入 axios.js: https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js

2. 使用 axios 函数

   - 传入配置对象
   - 再用 .then 回调函数接收结果，并作后续处理

   ```html
   axios({
   	url:'目标资源地址'   
   }).then((result)=>{
       // 对服务器返回的数据做后续处理
   })
   ```

   http://hmajax.itheima.net/api/province

