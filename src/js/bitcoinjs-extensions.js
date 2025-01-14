bitcoinjs.bitcoin.networks.groestlcoin = {
  messagePrefix: '\x1cGroestlCoin Signed Message:\n',
  bech32: 'grs',
  bip32: {
    public: 0x0488b21e,
    private: 0x0488ade4
  },
  pubKeyHash: 0x24,
  scriptHash: 0x05,
  wif: 0x80
};

bitcoinjs.bitcoin.networks.decred = {
  messagePrefix: 'unused',
  bip32: {
    public: 0x02fda926,
    private: 0x02fda4e8
  },
  pubKeyHash: 0x073f,
  scriptHash: 0x071a,
  wif: 0x80
};

bitcoinjs.bitcoin.networks.monero = {
    messagePrefix: 'x18XMR Signed Message:\n',
    bip32: {
      public: 0x0488B21E,
      private: 0x0488ADE4,
    },
    pubKeyHash: 0x7F,
    scriptHash: 0xC4,
    wif: 0x3F,
};
