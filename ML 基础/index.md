# AUC
对样本抽样预测，预测值一般都是[0,1]的小数。选取截断点来判断预测的结果。AUC 曲线相当于不听移动截断点来得到结果。
AUC 越靠近左上角，FPR 较小趋于零，也就是分类器对于正样本的打分要大于负样本。
- 衡量的是一种排序能力，所以特别适合排序类业务
坐标轴:
- y: TPR true positive rate
    - the ratio of true for all predicted positive samples
    - TP / (TP + FN) （正样本）
- x: FPR false positive rate
    - TN / (TN + FP) (负样本)