# sgd
w_new = w_old - alpha * g
# momentum
m_new = beta * m_old + (1 - beta) * g
w_new = w_old - alpha * m_new

# adagrad
v_new = v_old + g ** 2
w_new = w_old - alpha * (1 / sqrt(v_new) + epsilon) * g

# RMSProp
v_new = beta * v_old + (1-beta) * g ** 2
w_new = w_old - alpha * (1 / sqrt(v_new) + epsilon) * g

# Adam
m_new = beta_1 * m_old + (1-beta_1) * g  # first order
v_new = beta_2 * v_old + (1-beta_2) * g ** 2 # second order
# correct
m_new = m_new / (1 - beta_1^t)
v_new = v_new / (1 - beta_2^t)
# update
w_new = w_old - alpha * m_new / (sqrt(v_new) + epsilon)