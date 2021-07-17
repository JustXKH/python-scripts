
for m in model.modules():
    if isinstance(m, nn.Conv2d):
        n = m.kernel_size[0] * m.kernel_size[1] * m.out_channels
        m.weight.data.normal_(0, math.sqrt(2. / n))
    elif isinstance(m, nn.BatchNorm2d):
        m.weight.data.fill_(1)
        m.bias.data.zero_()




import torch.nn.init as init
if not args.resume:
    print('Initializing weights...')
    # initialize newly added layers' weights with xavier method
    refinedet_net.extras.apply(weights_init)
    refinedet_net.arm_loc.apply(weights_init)
    refinedet_net.arm_conf.apply(weights_init)
    refinedet_net.odm_loc.apply(weights_init)
    refinedet_net.odm_conf.apply(weights_init)
    #refinedet_net.tcb.apply(weights_init)
    refinedet_net.tcb0.apply(weights_init)
    refinedet_net.tcb1.apply(weights_init)
    refinedet_net.tcb2.apply(weights_init)

def xavier(param):
    init.xavier_uniform_(param)

def weights_init(m):
    if isinstance(m, nn.Conv2d):
        xavier(m.weight.data)
        m.bias.data.zero_()
    elif isinstance(m, nn.ConvTranspose2d):
        xavier(m.weight.data)
        m.bias.data.zero_()