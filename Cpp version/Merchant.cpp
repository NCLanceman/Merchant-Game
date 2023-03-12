// Merchant.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define roll(x, y) x*(rand()%y+1)


struct Location {
    unsigned char id; 
    char name[20]; 
    char description[200];
    unsigned char entry_fee; 
    float econ_scalar; 
    struct Location * previous, * next; 
};

struct Merchant {
    int gold, skill, security; 
    char name[10] = "Bill\0";
    void setup() {
        gold = roll(5, 4); 
        skill = roll(3, 6);
        security = roll(3, 6);
    }
} Bill;

void Populate(struct Location locations[]);

int main()
{   
    char game_loop = 1; 
    srand(time(NULL));
    struct Location locations[4]; 
    Populate(locations);
    Bill.setup(); 



    while (game_loop) {
        printf("Merchant Bill has %i gold, %i skill, and %i security.", Bill.gold, Bill.skill, Bill.security); 
        game_loop--; 
    }
    return 0; 
}

void Populate(struct Location locations[]) {
    struct Location first = { 1, "Hatterton", "An idyllic hamlet.", 5, 0.5f, &(locations[0]), &(locations[1])}; 
    struct Location second = { 2, "Mugambi", "A smattering of huts guarded by lean, fierce men who remain perpetually painted for war, despite the savannah heat.", 10, 0.3f, &(locations[0]), &(locations[2]) };
    struct Location third = { 3, "Nabooru", "Cherry blossoms and the perpetual smell of fish.", 20, 0.8f, &(locations[1]), &(locations[3]) };
    struct Location fourth = { 4, "Pupland", "Everything is waggy and wonderful.", 0, 1.0f, &(locations[2]), &(locations[4]) };
    locations[0] = first; 
    locations[1] = second; 
    locations[2] = third; 
    locations[3] = fourth; 
}