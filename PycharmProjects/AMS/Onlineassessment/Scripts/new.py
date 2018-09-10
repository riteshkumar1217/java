from Onlineassessment.Scripts.testpreview import TestPreview


class NewTest(TestPreview):

    def __init__(self):
        super(NewTest, self).__init__()
        self.test_run()
        self.tearDown()

    def test_run(self):
        print 'test_run successfully'
        pass


obj = NewTest()