from brownie import FundMe, MockV3Aggregator, network, config
from scripts.helpful_scripts import (
    get_account,
    deploy_mocks,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)


def deploy_fund_me():
    account = get_account()
    # Deploying FundMe while verifying and publishing the source code
    # and passing the price feed address the constructor

    # If on a persistent network like rinkeby, pass the associated price feed address
    # If not, deploy a mock
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        # Get the price feed from the config for the active network
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        # .get verify prevents index issues
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"The Contract has been deployed to {fund_me.address}")
    # returning fund_me for the test to interact with
    return fund_me


def main():
    deploy_fund_me()
