class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], vegan_friendly: int, max_price: int, max_distance: int) -> List[int]:
        res_rating_id = []
        for id, rating, veg, price, dist in restaurants:
            if (
                not veg and vegan_friendly or
                price > max_price or 
                dist > max_distance
            ):
                continue
            
            res_rating_id.append([rating, id])
        
        res = [id for rating, id in sorted(res_rating_id, reverse=True)]
        return res
             