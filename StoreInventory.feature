Feature: Verify the Store Inventory
      Scenario: Access pet store url and return pet inventories by status
            Given User is login with valid credentials
            When User access pet store and finds pet inventories by status
            Then Post a New Order for Pet



      Scenario : User User delete valid purchase order id
            Given User is login with valid credentials
            When User Delete the valid purchase order
            Then User logs out


      Scenario: User tries to find purchase order using incorrect order id
            Given User is login with valid credentials
            When User Get the purchase order by passing invalid order id
            Then Give Error Order not found