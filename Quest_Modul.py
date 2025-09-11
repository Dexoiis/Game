class Quest:
    """Einfaches Quest-Objekt mit Beschreibung, Zielen und Belohnungen."""
    def __init__(self, description, objectives, rewards=None):
        # objectives: Liste von Dicts {type: 'kill'/'collect', 'target': str, 'required': int, 'current': 0}
        self.description = description
        self.objectives = objectives
        self.rewards = rewards or []
        self.completed = False

    def update(self, event_type, target):
        """Aktualisiert den Fortschritt basierend auf Ereignis."""
        changed = False
        for obj in self.objectives:
            if obj.get("type") == event_type and obj.get("target") == target:
                if obj.get("current", 0) < obj.get("required", 0):
                    obj["current"] = obj.get("current", 0) + 1
                    changed = True
        if changed and all(o.get("current", 0) >= o.get("required", 0) for o in self.objectives):
            self.completed = True
        return changed

    def to_dict(self):
        return {
            "description": self.description,
            "objectives": self.objectives,
            "rewards": self.rewards,
            "completed": self.completed,
        }

    @classmethod
    def from_dict(cls, data):
        q = cls(data.get("description", ""), data.get("objectives", []), data.get("rewards", []))
        q.completed = data.get("completed", False)
        return q


class QuestManager:
    """Verwaltet aktive und abgeschlossene Quests."""
    def __init__(self, active=None, completed=None):
        self.active = active or []
        self.completed = completed or []

    def add_quest(self, quest):
        self.active.append(quest)

    def update_progress(self, event_type, target):
        for quest in list(self.active):
            if quest.update(event_type, target) and quest.completed:
                self.active.remove(quest)
                self.completed.append(quest)

    def get_status(self):
        if not self.active:
            return "Keine aktiven Quests."
        lines = []
        for q in self.active:
            lines.append(q.description)
            for obj in q.objectives:
                cur = obj.get("current", 0)
                req = obj.get("required", 0)
                target = obj.get("target", "")
                lines.append(f"  {target}: {cur}/{req}")
        return "\n".join(lines)

    def to_dict(self):
        return {
            "active": [q.to_dict() for q in self.active],
            "completed": [q.to_dict() for q in self.completed],
        }

    @classmethod
    def from_dict(cls, data):
        active = [Quest.from_dict(q) for q in data.get("active", [])]
        completed = [Quest.from_dict(q) for q in data.get("completed", [])]
        return cls(active, completed)
