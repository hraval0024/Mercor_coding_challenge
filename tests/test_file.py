import unittest
from referral.network import ReferralNetwork, ReferralError

class TestReferralNetwork(unittest.TestCase):
    def setUp(self):
        self.net = ReferralNetwork()
        self.net.add_referral("r1", "c1")
        self.net.add_referral("r1", "c2")
        self.net.add_referral("c1", "c3")

    def test_direct_all_referrals(self):
        self.assertSetEqual(set(self.net.direct_referrals("r1")), {"c1","c2"})
        self.assertSetEqual(self.net.all_referrals("r1"), {"c1","c2","c3"})

    def test_cycle_detection(self):
        with self.assertRaises(ReferralError):
            self.net.add_referral("c3", "r1")

if __name__ == "__main__":
    unittest.main()