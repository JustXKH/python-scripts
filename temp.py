import os

# s = ('%10s' * 2 + '%10s' * 6) % ('%s/%s'% ('epoch', 'epochs' ), 'mem', 'GIoU_loss','obj_loss','cls_loss', '#targets', 'img_size')
# print()
        # Write epoch results
        # with open(results_file, 'a') as f:
        #     f.write(s + '%10.3g' * 7 % results + '\n')  # P, R, mAP, F1, test_losses=(GIoU, obj, cls)
t =('%10s'*6)%('mem', 'GIoU_loss','obj_loss','cls_loss', '#targets', 'img_size')
s = ('%10s' * 2 )%('%s/%s'% ('epoch', 'epochs' ))
with open('results.txt', 'w') as fp:
    fp.write(s + t)