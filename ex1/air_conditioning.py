class AirConditioning:
    """
    Class of air conditioning.

    Args:
        __status (bool): status of air conditioning
        __temperature (float): temperature of air condotioning
    """

    def __init__(self):
        """
        The function initialises an instance of the molecule class.
        """
        self.__status = False  # Значение по умолчанию: выключен
        self.__temperature = None  # Значение по умолчанию: 18°C

    @property
    def status(self):
        """
        Function for obtaining the status of the air conditioner.
        :return: status
        """

        return self.__status

    @property
    def temperature(self):
        """
        Function for obtaining the temperature of the air conditioner.
        :return: temperature
        """

        return self.__temperature

    @status.setter
    def status(self, value):
        """
        Function for setting the new status of the air conditioner.
        :param value: value of conditioner
        """
        self.__status = self.__status

    @temperature.setter
    def temperature(self, value):
        """
        Function for setting a new temperature for the air conditioner.
        :param value: value of temperature
        :return:
        """
        self.__temperature = self.__temperature

    def switch_on(self):
        """
        Function for switching on the air conditioner.
        """
        if self.__status is False:
            self.__status = True
            self.__temperature = 18

    def switch_off(self):
        """
        Function for switching off the air conditioner.
        """
        self.__status = False

    def reset(self):
        """
        Function for resetting the temperature of the air conditioner 18.
        """
        if self.__status:
            self.__temperature = 18

    def get_temperature(self):
        """
        The function returns the current temperature of the air conditioner.
        :return: current temperature
        """
        return self.__temperature

    def raise_temperature(self):
        """
        The function increases the temperature of the air conditioner by 1 degree.
        """
        if self.__temperature is not None and self.__temperature < 43:
            self.__temperature += 1

    def lower_temperature(self):
        """
        The function reduces the temperature of the air conditioner by 1 degree.
        """
        if self.__temperature is not None and self.__temperature > 0:
            self.__temperature -= 1

    def __str__(self):
        if self.__status is True:
            return f'Кондиционер включен. Температурный режим: {self.__temperature} градусов.'
        else:
            return 'Кондиционер выключен.'

    def __repr__(self):
        return self.__str__()
