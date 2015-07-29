/*
 * @turlapatykaushik
 * github url : github.com/turlapatykaushik
 * problem description : Mark and Toys
*/


def maximum_toys(prices, budget):
    number_of_toys = 0
    total_price = 0
    for i in sorted(prices):
        if total_price + i <= budget:
            number_of_toys += 1
            total_price += i
        else:
            break
    return number_of_toys

if __name__ == '__main__':
    total_toys, budget = map(int, raw_input().split())
    prices = map(int, raw_input().split())
    print maximum_toys(prices, budget)
