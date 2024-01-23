import { StacksMainnet } from '@stacks/network';
import {
  callReadOnlyFunction,
  contractPrincipalCV,
  cvToJSON,
  uintCV,
  falseCV,
} from '@stacks/transactions';
import * as fs from 'fs';

console.log(process.argv[2])
const vaultid = process.argv[2]
const contractAddress = 'SP2C2YFP12AJZB4MABJBAJ55XECVS7E4PMMZ89YZR';
const contractName = 'arkadiko-freddie-v1-1';
const functionName = 'get-vault-by-id';
const senderAddress = 'ST2F4BK4GZH6YFBNHYDDGN4T1RKBA7DA1BJZPJEJJ';
const network = new StacksMainnet();
const options = {
  contractAddress,
  contractName,
  functionName,
  functionArgs: [
  	uintCV(vaultid),
        ],
  network,
  senderAddress,
};

const result = await callReadOnlyFunction(options);
const json = cvToJSON(result);
console.log(json)

fs.writeFile('all/'+vaultid+'.json', JSON.stringify(json), err => {
  if (err) {
    console.error(err);
  }
  // file written successfully
});
