multiples3and5 :: Int -> Int -> Int
multiples3and5 end sum
	| end == 0 = sum
	| end `mod` 3 == 0 = multiples3and5 (end - 1) (sum + end)
	| end `mod` 5 == 0 = multiples3and5 (end - 1) (sum + end)
	| otherwise    = multiples3and5 (end - 1) sum

main :: IO ()
main = print (multiples3and5 999 0)