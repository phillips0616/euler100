fibsum :: Int -> Int -> Int -> Int
fibsum prev cur sum
    | cur > 4000000                        = sum
    | (cur <= 4000000 && cur `mod` 2 == 0) = fibsum cur (prev + cur) (sum + cur)
    | otherwise                            = fibsum cur (prev + cur) sum

main :: IO ()
main = print(fibsum 1 2 0)