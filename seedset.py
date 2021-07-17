# reason: 实验结果的再现性reproducibiliy,每次实验结果的近似一致性
# Set random seeds
torch.backends.cudnn.deterministic = True
torch.manual_seed(args.random_seed)
if torch.cuda.is_available():
    torch.cuda.manual_seed_all(args.random_seed)
np.random.seed(args.random_seed)
random.seed(args.random_seed)

# set seeds
random.seed(args.seed)
os.environ['PYTHONHASHSEED'] =str(args.seed)
np.random.seed(args.seed)
torch.manual_seed(args.seed)
torch.cuda.manual_seed(args.seed)
torch.cuda.manual_seed_all(args.seed)
torch.backends.cudnn.deterministic =True
