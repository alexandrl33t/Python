#pragma
#include <tuple>
#include <vector>
#include <algorithm>

template<typename Model>
class Tester
{
    Model& model;
public:
    Tester(Model& model): model{model} {}

    template<typename ... Args>
    auto make_test(Args ... args)
    {
        return model(args...);
    }

    template<typename RetType, typename ... Args>
    auto make_tests(const std::vector<std::tuple<Args...>>& inputs)
    {
        auto mt([&](auto ...args){
            return model(args...);
        });
        
        std::vector<RetType> res;
        res.reserve(inputs.size());

        transform(begin(inputs), end(inputs), back_inserter(res), [&](auto tupl){
            return apply(mt, tupl);
        });
        return res;
    }

    auto make_simple_tests(size_t count)
    {
        std::vector<double> res(count);

        generate(begin(res), end(res), model);

        return res;
    }
};




