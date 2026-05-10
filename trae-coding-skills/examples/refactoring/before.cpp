// ❌ 反例：长函数、重复逻辑、大类

#include <iostream>
#include <vector>
#include <string>

class OrderProcessor {
public:
    void process(const std::vector<std::string>& items, const std::string& customerType, double total) {
        double discount = 0.0;
        if (customerType == "VIP") {
            if (total > 1000) {
                discount = total * 0.2;
            } else if (total > 500) {
                discount = total * 0.15;
            } else {
                discount = total * 0.1;
            }
        } else if (customerType == "MEMBER") {
            if (total > 1000) {
                discount = total * 0.15;
            } else if (total > 500) {
                discount = total * 0.1;
            } else {
                discount = total * 0.05;
            }
        } else {
            if (total > 1000) {
                discount = total * 0.05;
            }
        }

        double finalTotal = total - discount;

        std::cout << "Items:" << std::endl;
        for (size_t i = 0; i < items.size(); ++i) {
            std::cout << "  - " << items[i] << std::endl;
        }

        std::cout << "Customer: " << customerType << std::endl;
        std::cout << "Original: " << total << std::endl;
        std::cout << "Discount: " << discount << std::endl;
        std::cout << "Final: " << finalTotal << std::endl;

        if (finalTotal > 0) {
            std::cout << "Status: PAID" << std::endl;
        } else {
            std::cout << "Status: FREE" << std::endl;
        }
    }
};
