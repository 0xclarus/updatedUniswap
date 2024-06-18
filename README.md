## Foundry
 
 **REWRITING SOLIDITY IN THE LATEST VERSION AND IN FOUNDRY  .**
 ```
 $ upgrades from solidity v0.5.16 to 0.8.19.

 EDITED MINT() in UniswapV2ERC20.sol
 ```

**Foundry is a blazing fast, portable and modular toolkit for Ethereum application development written in Rust.**

Foundry consists of:

-   **Forge**: Ethereum testing framework (like Truffle, Hardhat and DappTools).
-   **Cast**: Swiss army knife for interacting with EVM smart contracts, sending transactions and getting chain data.
-   **Anvil**: Local Ethereum node, akin to Ganache, Hardhat Network.
-   **Chisel**: Fast, utilitarian, and verbose solidity REPL.

## Documentation

https://book.getfoundry.sh/

## Usage

### Build

```shell
$ forge build
```

### Test

```shell
$ forge test
```

### Format

```shell
$ forge fmt
```

### Gas Snapshots

```shell
$ forge snapshot
```

### Anvil

```shell
$ anvil
```

### Deploy

```shell
$ forge script script/Counter.s.sol:CounterScript --rpc-url <your_rpc_url> --private-key <your_private_key>
```

### Cast

```shell
$ cast <subcommand>
```

### Help

```shell
$ forge --help
$ anvil --help
$ cast --help
```

Contracts and functions

- Factory()
A smart contract that deploys a unique smart contract for any ERC20/ERC20 trading pair.

Pair
A smart contract deployed from the Uniswap V2 Factory that enables trading between two ERC20 tokens.

# REPLACING ALL REQUIRE WITH CUSTOM ERRORS.
 ## First, More Gas efficient
 ## Secondly, makes it readable and i learn more 

