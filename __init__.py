from mycroft import MycroftSkill, intent_file_handler


class DateTimeFrancais(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('francais.time.date.intent')
    def handle_francais_time_date(self, message):
        self.speak_dialog('francais.time.date')


def create_skill():
    return DateTimeFrancais()

