class WizCoinException(Exception):
	"""Exceptions of the WizCoin class."""
	pass


class WizCoin:
	def __init__(self, galleons, sickles, knuts):
		self.galleons = galleons
		self.sickles  = sickles
		self.knuts    = knuts

	@property
	def total(self):
		return self.galleons + self.sickles + self.knuts

	@property
	def galleons(self):
		return self._galleons

	@galleons.setter
	def galleons(self, value):
		if not isinstance(value, int):
			message = f"Wizcoin ammount must be an int, but {value.__class__.__qualname__} was given."
			raise WizCoinException(message)
		self._galleons = value

	@galleons.deleter
	def galleons(self):
		print("deleting galleons attribute.")
		del self._galleons


	@property
	def sickles(self):
		return self._sickles

	@sickles.setter
	def sickles(self, value):
		if not isinstance(value, int):
			message = f"Wizcoin ammount must be an int, but {value.__class__.__qualname__} was given."
			raise WizCoinException(message)
		self._sickles = value

	@sickles.deleter
	def sickles(self):
		print("deleting sickles attribute.")
		del self._sickles


	@property
	def knuts(self):
		return self._knuts

	@knuts.setter
	def knuts(self, value):
		if not isinstance(value, int):
			message = f"Wizcoin ammount must be an int, but {value.__class__.__qualname__} was given."
			raise WizCoinException(message)
		self._knuts = value

	@knuts.deleter
	def knuts(self):
		print("deleting knuts attribute.")
		del self._knuts


	def __repr__(self):
		"""Returns a string of the expression that recreates the object."""
		return f"{self.__class__.__qualname__}({self.galleons}, {self.sickles}, {self.knuts})"

	def __str__(self):
		"""Returns a string representation of the WizCoin object that humans can easily understand."""
		return f"{self.galleons} galleons, {self.sickles} sickles, {self.knuts} knuts"

	def __len__(self):
		return self.galleons + self.sickles  + self.knuts

	def __add__(self, other):
		if not isinstance(other, WizCoin):
			return NotImplemented
		return WizCoin(other.galleons+self.galleons, other.sickles + self.sickles, other.knuts + self.knuts)

	def __mul__(self, other):
		if not isinstance(other, int):
			return NotImplemented

		if other < 0:
			raise WizCoinException("Cannot multiply by negative integer.")

		return WizCoin(self.galleons*other, self.sickles*other, self.knuts*other)

	def __rmul__(self, other):
		if not isinstance(other, int):
			return NotImplemented

		if other < 0:
			raise WizCoinException("Cannot multiply by negative integer.")

		return WizCoin(self.galleons*other, self.sickles*other, self.knuts*other)

	def __eq__(self, other):
		if not isinstance(other, WizCoin):
			return False
		return all([self.galleons==other.galleons, self.sickles==other.sickles, self.knuts==other.knuts])

	def __ne__(self, other):
		if not isinstance(other, WizCoin):
			return True
		return False == all([self.galleons==other.galleons, self.sickles==other.sickles, self.knuts==other.knuts])





	