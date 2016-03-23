#!/usr/bin/python
# -*- coding:utf-8 -*-

import unittest
from earo.event import Event
from earo.handler import Handler, Emittion, NoEmittion
from earo.mediator import Mediator
from earo.context import Context
from earo.processor import ProcessFlow, Processor
from earo.diagram import Diagram


class TestDiagram(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_html(self):

        mediator = Mediator()
        processor = Processor()

        class EventA(Event):
            pass

        class EventB(Event):
            pass

        class EventC(Event):
            pass

        class EventD(Event):
            pass

        def fooBC(context, event):
            return (Emittion(EventB()), Emittion(EventC()))

        def fooD(context, event):
            return Emittion(EventD())

        def foo(context, event):
            pass

        def fooEx(context, event):
            1 / 0

        handler_1 = Handler(EventA, fooBC, [EventB, EventC])
        handler_2 = Handler(EventA, foo)
        handler_3 = Handler(EventB, fooD, [EventD])
        handler_4 = Handler(EventC, foo)
        handler_5 = Handler(EventD, fooEx)

        mediator.register_event_handler(
            handler_1,
            handler_2,
            handler_3,
            handler_4,
            handler_5
        )

        context = Context(mediator, EventA(), processor)
        context.process()
        process_flow = context.process_flow

        diagram = Diagram(process_flow)
        diagram.transfer_process_flow_to_html('/tmp/earo')

if __name__ == '__main__':
    unittest.main()
