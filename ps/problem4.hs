isPalindrome :: Int -> Bool
isPalindrome x = show x == reverse (show x) 

lgPalindrome :: Int -> Int -> Int -> Int
lgPalindrome a b cur
	| a == 1 = cur
	| a * b > cur && isPalindrome(a * b) = lgPalindrome (a - 1) (a - 1) (a * b)
	| a * b > cur = lgPalindrome a (b - 1) cur
	| otherwise = lgPalindrome (a - 1) (a - 1) cur
	

main :: IO()
main = print(lgPalindrome 999 999 0)