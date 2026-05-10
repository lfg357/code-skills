// ✅ 正例：提取函数、表驱动、职责分离

#include <iostream>
#include <vector>
#include <string>
#include <functional>
#include <map>

struct DiscountRule {
    double threshold;
    double rate;
};

using DiscountTable = std::vector<DiscountRule>;

class DiscountCalculator {
public:
    explicit DiscountCalculator(const DiscountTable& rules) : rules_(rules) {}

    double calculate(double total) const {
        for (const auto& rule : rules_) {
            if (total > rule.threshold) {
                return total * rule.rate;
            }
        }
        return 0.0;
    }

private:
    DiscountTable rules_;
};

class ReceiptPrinter {
public:
    void print(const std::vector<std::string>& items,
               const std::string& customerType,
               double original,
               double discount,
               double finalTotal) const {
        printItems(items);
        printSummary(customerType, original, discount, finalTotal);
    }

private:
    void printItems(const std::vector<std::string>& items) const {
        std::cout << "Items:" << std::endl;
        for (const auto& item : items) {
            std::cout << "  - " << item << std::endl;
        }
    }

    void printSummary(const std::string& customerType,
                      double original,
                      double discount,
                      double finalTotal) const {
        std::cout << "Customer: " << customerType << std::endl;
        std::cout << "Original: " << original << std::endl;
        std::cout << "Discount: " << discount << std::endl;
        std::cout << "Final: " << finalTotal << std::endl;
        std::cout << "Status: " << (finalTotal > 0 ? "PAID" : "FREE") << std::endl;
    }
};

class OrderProcessor {
public:
    OrderProcessor() {
        calculators_["VIP"] = DiscountCalculator({{1000, 0.2}, {500, 0.15}, {0, 0.1}});
        calculators_["MEMBER"] = DiscountCalculator({{1000, 0.15}, {500, 0.1}, {0, 0.05}});
        calculators_["GUEST"] = DiscountCalculator({{1000, 0.05}});
    }

    void process(const std::vector<std::string>& items,
                 const std::string& customerType,
                 double total) const {
        double discount = getDiscount(customerType, total);
        double finalTotal = total - discount;

        ReceiptPrinter printer;
        printer.print(items, customerType, total, discount, finalTotal);
    }

private:
    double getDiscount(const std::string& customerType, double total) const {
        auto it = calculators_.find(customerType);
        if (it != calculators_.end()) {
            return it->second.calculate(total);
        }
        return 0.0;
    }

    std::map<std::string, DiscountCalculator> calculators_;
};
