from brownie import FundMe
from scripts.helpful_scripts import get_account


def fund():
    # Set variable fund_me to the latest deployment of the FundMe contract
    fund_me = FundMe[-1]
    account = get_account()
    entrance_fee = fund_me.getEntranceFee()
    print(entrance_fee)
    print(f"The current entry fee is {entrance_fee}")
    print("Funding")
    fund_me.fund({"from": account, "value": entrance_fee})


def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    fund_me.withdraw({"from": account})


# 0.025000000000000000 ether (at 1 ETH = $2000)
def main():
    fund()
    withdraw()
