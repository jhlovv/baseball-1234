class Game:
    def guess(self, guessNumber):
        self.assert_illegal_value(guessNumber)

    def assert_illegal_value(self, guessNumber):
        if guessNumber is None:
            raise TypeError()
        if len(guessNumber) != 3:
            raise TypeError()
        for number in guessNumber:
            if not ord('0') <= ord(number) <= ord('9'):
                raise TypeError()
        if self.isDuplicaedNumber(guessNumber):
            raise TypeError()

    def isDuplicaedNumber(self, guessNumber):
        return len(set(guessNumber)) != 3