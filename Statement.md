**Problem Statement**
In many small to medium-scale retail environments, specifically boutique clothing stores, the reliance on manual billing methods or outdated physical ledgers creates significant operational inefficiencies. Manual calculations are prone to human error, leading to financial discrepancies and customer dissatisfaction. Furthermore, the process of handwriting receipts is time-consuming, causing long queues during peak hours. There is a lack of a centralized, automated method to quickly view product prices and generate professional, timestamped records of transactions, which hinders the store's ability to maintain a professional image and ensure accounting accuracy.

**Scope of the Project**
The scope of this project is to develop a robust, console-based Billing Management System tailored for a clothing retailer dealing in Western wear, Ethnic wear, and Accessories. The system is designed to digitize the checkout process entirely. It encompasses the creation of a digital product repository that allows for instant price retrieval, a dynamic shopping cart system that accepts user inputs for product codes and quantities, and a logic layer that handles all arithmetic calculations automatically. The project boundaries currently focus on the frontend transaction processing within a Command Line Interface (CLI), operating on local storage without the need for external database connectivity or internet access, ensuring high speed and reliability.

**Target Users**
The primary target users for this application include:
1.  **Small Business Owners:** Proprietors of boutique clothing shops who need a cost-effective, digital solution to manage sales without investing in expensive enterprise ERP software.
2.  **Cashiers and Billing Clerks:** Staff members responsible for the checkout counter who require a tool to speed up the billing process and eliminate mental math errors.
3.  **Store Managers:** Individuals who need to quickly verify product prices and catalog details to assist customers on the floor.

**High-level features**
* **Categorized Product Catalog:** The system features a comprehensive, pre-loaded database of products (ranging from Western tops to Ethnic kurtas and accessories), displaying them in a cleanly formatted table with codes and prices for easy reference.
* **Dynamic Cart Management:** Users can iteratively add items to a virtual shopping basket. The system supports multiple entries, allowing the cashier to build a complete order line-by-line using unique product identifiers.
* **Robust Input Validation:** To prevent system crashes and ensure data integrity, the application includes error-handling mechanisms. It automatically rejects invalid product codes and non-numeric quantity inputs, prompting the user for corrections immediately.
* **Real-time Financial Calculation:** As items are added, the system automatically calculates line totals (Price × Quantity) and updates the running grand total, providing immediate feedback on the transaction value.
* **Automated Receipt Generation:** Upon concluding a sale, the system generates a final, timestamped receipt. This digital bill itemizes every purchased product, displays unit prices and total costs, and serves as a professional record of the transaction.
