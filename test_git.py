import torch

t_a = torch.randn([3, 5], dtype=torch.half)
t_b = torch.randn([3, 5], dtype=torch.float)

# test a plus
t_c = t_a + t_b

print(t_c)