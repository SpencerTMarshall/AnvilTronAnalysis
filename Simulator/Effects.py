import Simulator.MagicSim as MagicSim
from copy import deepcopy as cpy

class State:
    def __init__(self, bf: MagicSim.Battlefield, gy: MagicSim.Graveyard, lb: MagicSim.Library, hd: MagicSim.Hand, st: MagicSim.Stack, ld: int):
        self.bf = bf
        self.gy = gy
        self.lb = lb
        self.hd = hd
        self.st = st
        self.land = ld
        self.mana = [0,0]

class Uncastable(MagicSim.Card):
    def __init__(self):
        self.name = "Uncastable"
        self.tapped = None
        self.types = []
        self.subtypes = []
        self.colour = "Green"
        self.cost = [10,10]
        self.abilities = []

    def effect(self, state: State):
        pass

class Forest(MagicSim.Card):
    def __init__(self):
        self.name = "Forest"
        self.tapped = None
        self.types = ["Basic", "Land"]
        self.subtypes = ["Forest"]
        self.colour = "Colourless"
        self.cost = [0,0]
        self.produce = [0,1]
        self.abilities = []

    def effect(self, state: State) -> [State]:
        temp = cpy(state)
        temp.st.cardList[0].tapped = False

        temp.bf.addToTop(temp.st.cardList[0])

        temp.st.cardList = []

        return [temp]

class ColourlessLand(MagicSim.Card):
    def __init__(self):
        self.name = "CLand"
        self.tapped = None
        self.types = ["Land"]
        self.subtypes = []
        self.colour = "Colourless"
        self.cost = [0,0]
        self.produce = [1,0]
        self.abilities = []

    def effect(self, state: State):
        temp = cpy(state)
        temp.st.cardList[0].tapped = False

        temp.bf.addToTop(temp.st.cardList[0])

        temp.st.cardList = []

        return [temp]

class UrzasPowerPlant(MagicSim.Card):
    def __init__(self):
        self.name = "Urza's Power Plant"
        self.tapped = None
        self.types = ["Land"]
        self.subtypes = ["Urza's", "Power-Plant"]
        self.colour = "Colourless"
        self.cost = [0,0]
        self.produce = [1,0]
        self.abilities = []
    
    def effect(self, state: State):
        temp = cpy(state)
        temp.st.cardList[0].tapped = False

        temp.bf.addToTop(temp.st.cardList[0])

        temp.st.cardList = []

        return [temp]

class UrzasMine(MagicSim.Card):
    def __init__(self):
        self.name = "Urza's Mine"
        self.tapped = None
        self.types = ["Land"]
        self.subtypes = ["Urza's", "Mine"]
        self.colour = "Colourless"
        self.cost = [0,0]
        self.produce = [1,0]
        self.abilities = []

    def effect(self, state: State):
        temp = cpy(state)
        temp.st.cardList[0].tapped = False

        temp.bf.addToTop(temp.st.cardList[0])

        temp.st.cardList = []

        return [temp]


class UrzasTower(MagicSim.Card):
    def __init__(self):
        self.name = "Urza's Tower"
        self.tapped = None
        self.types = ["Land"]
        self.subtypes = ["Urza's", "Tower"]
        self.colour = "Colourless"
        self.cost = [0,0]
        self.produce = [1,0]
        self.abilities = []

    def effect(self, state: State):
        temp = cpy(state)
        temp.st.cardList[0].tapped = False

        temp.bf.addToTop(temp.st.cardList[0])

        temp.st.cardList = []

        return [temp]

class CandyTrail(MagicSim.Card):
    class CandyTrailAbility(MagicSim.Ability):
        cost = [2,0]

        def effect(state: State):
            temp = cpy(state)

            x = 0
            while x < len(temp.bf.cardList):
                if temp.bf.cardList[x].name == "Candy Trail":
                    temp.bf.cardList[x].tapped = None
                    temp.gy.addToTop(temp.bf.cardList[x])
                    temp.bf.cardList = temp.bf.cardList[:x] + temp.bf.cardList[x+1:]
                x+=1
            
            temp.hd.addToTop(temp.lb.takeFromTop())
            return [temp]
        
    def __init__(self):
        self.name = "Candy Trail"
        self.tapped = None
        self.types = ["Artifact"]
        self.subtypes = ["Food", "Clue"]
        self.colour = "Colourless"
        self.cost = [1,0]
        self.abilities = [self.CandyTrailAbility]
    
    def effect(self, state: State):
        res = [cpy(state) for x in range(6)]

        for s in res:
            # Move candy trail to battlefield
            s.st.cardList[0].tapped = False
            s.bf.addToTop(s.st.takeFromTop())

        # 2 top same order
        res[0]

        # 2 top rev order
        xs = [res[1].lb.takeFromTop() for x in range(2)]
        for x in xs:
            res[1].lb.addToTop(x)

        # 1 top 1 bot same order
        xs = [res[2].lb.takeFromTop() for x in range(2)]
        res[2].lb.addToTop(xs[0])
        res[2].lb.addToBottom(xs[1])

        # 1 top 1 bot rev order
        xs = [res[3].lb.takeFromTop() for x in range(2)]
        res[2].lb.addToTop(xs[1])
        res[2].lb.addToBottom(xs[0])

        # 2 bot same order
        res[4].lb.addToBottom(res[4].lb.takeFromTop())
        res[4].lb.addToBottom(res[4].lb.takeFromTop())

        # 2 bot rev order
        xs = [res[5].lb.takeFromTop() for x in range(2)]
        res[5].lb.addToBottom(xs[1])
        res[5].lb.addToBottom(xs[0])

        return res

class ExpeditionMap(MagicSim.Card):
    class MapAbility(MagicSim.Ability):
        cost = [2,0]

        def effect(state: State):
            ans = []

            found_so_far = []
            for card in state.lb.cardList:
                if "Land" in card.types:
                    if card.name not in found_so_far:
                        found_so_far.append(card.name)

                        temp = cpy(state)
                        i = state.lb.cardList.index(card)

                        temp.hd.addToTop(temp.lb.cardList[i])
                        temp.lb.cardList = temp.lb.cardList[:i] + temp.lb.cardList[i+1:]

                        x = 0
                        while x < len(temp.bf.cardList):
                            if temp.bf.cardList[x].name == "Expedition Map":
                                temp.bf.cardList[x].tapped = None
                                temp.gy.addToTop(temp.bf.cardList[x])
                                temp.bf.cardList = temp.bf.cardList[:x] + temp.bf.cardList[x+1:]
                            x+=1
                        
                        temp.lb.shuffle()
                        ans.append(temp)
            
            return ans
    
    def __init__(self):
        self.name = "Expedition Map"
        self.tapped = None
        self.types = ["Artifact"]
        self.subtypes = []
        self.colour = "Colourless"
        self.cost = [1,0]
        self.abilities = [self.MapAbility]

    def effect(self, state):
        temp = cpy(state)
        temp.st.cardList[0].tapped = False
        temp.bf.addToTop(temp.st.cardList[0])
        temp.st.cardList = []
        return [temp]

class RelicOfProgenitus(MagicSim.Card):
    class RelicAbility(MagicSim.Ability):
        cost = [1,0]

        def effect(state: State):
            temp = cpy(state)

            x = 0
            while x < len(temp.bf.cardList):
                if temp.bf.cardList[x].name == "Relic of Progenitus":
                    temp.bf.cardList[x].tapped = None
                    temp.gy.addToTop(temp.bf.cardList[x])
                    temp.bf.cardList = temp.bf.cardList[:x] + temp.bf.cardList[x+1:]
                x+=1

            temp.hd.addToTop(temp.lb.takeFromTop())
            return [temp]
        
    def __init__(self):
        self.name = "Relic of Progenitus"
        self.tapped = None
        self.types = ["Artifact"]
        self.subtypes = []
        self.colour = "Colourless"
        self.cost = [1,0]
        self.abilities = [self.RelicAbility]

    def effect(self, state):
       temp = cpy(state)
       temp.st.cardList[0].tapped = False

       temp.bf.addToTop(temp.st.cardList[0])

       temp.st.cardList = []

       return [temp]


class ChromaticSphere(MagicSim.Card):
    class ChromaticSphereAbility(MagicSim.Ability):
        cost = [1,0]

        def effect(state: State):
            temp = cpy(state)
            
            x = 0
            while x < len(temp.bf.cardList):
                if temp.bf.cardList[x].name == "Chromatic Sphere":
                    temp.bf.cardList[x].tapped = None
                    temp.gy.addToTop(temp.bf.cardList[x])
                    temp.bf.cardList = temp.bf.cardList[:x] + temp.bf.cardList[x+1:]
                
                x+=1
  
            temp.hd.addToTop(temp.lb.takeFromTop())
            temp.mana[1] += 1

            return [temp]

    def __init__(self):
        self.name = "Chromatic Sphere"
        self.tapped = None
        self.types = ["Artifact"]
        self.subtypes = []
        self.colour = "Colourless"
        self.cost = [1,0]
        self.abilities = [self.ChromaticSphereAbility]

    def effect(self, state: State):
        temp = cpy(state)

        temp.st.cardList[0].tapped = False

        temp.bf.addToTop(temp.st.cardList[0])

        temp.st.cardList = []

        return [temp]

class Explore(MagicSim.Card):
    def __init__(self):
        self.name = "Explore"
        self.tapped = None
        self.types = ["Sorcery"]
        self.subtypes = []
        self.colour = "Green"
        self.cost = [1,1]
        self.abilities = []

    def effect(self, state: State) -> [State]:
        temp = cpy(state)

        temp.gy.addToTop(temp.st.cardList[0])

        temp.hd.addToTop(temp.lb.takeFromTop())

        temp.land += 1

        return [temp]

class SylvanScrying(MagicSim.Card):
    def __init__(self):
        self.name = "Sylvan Scrying"
        self.tapped = None
        self.types = ["Sorcery"]
        self.subtypes = []
        self.colour = "Green"
        self.cost = [1,1]
        self.abilities = []

    def effect(self, state: State) -> [State]:
        ans = []

        found_so_far = []
        for card in state.lb.cardList:
            if "Land" in card.types:
                if card.name not in found_so_far:
                    found_so_far.append(card.name)

                    temp = cpy(state)
                    temp.gy.addToTop(temp.st.takeFromTop())
                    i = state.lb.cardList.index(card)

                    temp.hd.addToTop(temp.lb.cardList[i])
                    temp.lb.cardList = temp.lb.cardList[:i] + temp.lb.cardList[i+1:]

                    temp.lb.shuffle()
                    ans.append(temp)
            
        return ans

class AncientStirrings(MagicSim.Card):
    def __init__(self):
        self.name = "Ancient Stirrings"
        self.tapped = None
        self.types = ["Sorcery"]
        self.subtypes = []
        self.colour = "Green"
        self.cost = [0,1]
        self.abilities = []

    def effect(self, state: State) -> [State]:
        def solveState(st: State, n: int) -> State:
            temp = cpy(state)
            temp.gy.addToTop(temp.st.takeFromTop())

            temp.hd.addToTop(temp.lb.cardList[n])

            for i in range(5):
                if i == n:
                    continue
                else:
                    temp.lb.addToBottom(temp.lb.cardList[i])
            
            temp.lb.cardList = temp.lb.cardList[5:]

            return temp

        ans = []

        for i in range(5):
           if state.lb.cardList[i].colour == "Colourless":
               ans.append(solveState(state, i))
        
        return ans