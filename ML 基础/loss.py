# MSE
L = 1/N(sum_i,k)(y_i - y_j)^2

# CrossEntropy

L = -1/N (sum_i_k)y_ilog(y_i^k)

'''
- 第一个是已知的 tag， one hot，例如 [0,0,1,0,0]
- 第二个是分类的预测输出    
    - 例如 [0, 0.7,0.1,0.1,0.1]
- 预测的时候，对应位置的预测概率越高，越接近 1，log(y_i^k) 越小，接近 0，取负数后乘值越小
- 越小，like 0.1, -log(0.1) 越大，损失越大


'''

# softmax
a = e^z0 / sum(e^zi)
