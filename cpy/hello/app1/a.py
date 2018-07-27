print('a 开始');
exports.done = false;
const b = require('./b.js');
print('在 a 中，b.done = %j', b.done);
exports.done = true;
print('a 结束');