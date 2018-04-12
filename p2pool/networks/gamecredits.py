from p2pool.bitcoin import networks

PARENT = networks.nets['gamecredits']
SHARE_PERIOD = 15 # seconds target spacing
CHAIN_LENGTH = 24*60*60//10 # shares
REAL_CHAIN_LENGTH = 24*60*60//10 # shares
TARGET_LOOKBEHIND = 100 # shares coinbase maturity
SPREAD = 10 # blocks
IDENTIFIER = '1c01cdd189b49f11'.decode('hex')
PREFIX = '1c01cdd3ddc08312'.decode('hex')
P2P_PORT = 2963
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = True
WORKER_PORT = 40004
BOOTSTRAP_ADDRS = 'p2p-spb.xyz p2p-south.xyz '.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-alt'
VERSION_CHECK = lambda v: True
SOFTFORKS_REQUIRED = set(['bip65', 'csv', 'segwit'])
SEGWIT_ACTIVATION_VERSION = 16

