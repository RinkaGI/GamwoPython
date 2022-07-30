import threading

class Timer:
    def __init__(self, duration) -> None:
        self.duration = duration
        self.action_handler = []

    def _setAction(self):
        for action in self.action_handler:
            action()

    def start(self):
        threading.Timer(self.duration, self._setAction).start()

    def setStartAction(self, action):
        self.action_handler.append(action)
        return action
