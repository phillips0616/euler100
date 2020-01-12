makeOdd :: Int -> Int
makeOdd n
	| n `mod` 2 /= 0 = n
	| otherwise = makeOdd (n `div` 2)
	
	
primeFactor :: Int -> Int -> Int -> Int
primeFactor n  sqrtn curFactor
	| n `mod` curFactor == 0 && n `div` curFactor /= 1 = primeFactor (n `div` curFactor) sqrtn curFactor
	| curFactor + 2 > sqrtn = n
	| otherwise = primeFactor n sqrtn (curFactor + 2)
	
x = makeOdd(600851475143)
sqrtx = floor(sqrt( fromIntegral x))

main :: IO()
main = do
	print(primeFactor x sqrtx  3)