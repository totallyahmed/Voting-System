nominee1 = input("Enter the name of the 1st Nominee : ")
nominee2 = input("Enter the name of the 2nd Nominee : ")

nm1_votes = 0 # initially votes are 0
nm2_votes = 0

voter_id = [1,2,3,4,5,6,7,8,9,10]

no_of_voter = len(voter_id)

while True:
    if voter_id == []: # to check when voter list is completed
        print("Voting session is over.")
        if nm1_votes > nm2_votes:
            percent = (nm1_votes/no_of_voter)*100
            print(nominee1,"has won with", percent,"% of votes")
            break
        elif nm2_votes > nm1_votes:
            percent = (nm2_votes/no_of_voter)*100
            print(nominee2, "has won with", percent,"% of votes")
            break
        else:
            print("It's a tie")
            break


    voter = int(input("Enter your Voter ID: "))
    if voter in voter_id:
        print("You are a voter.")
        voter_id.remove(voter) #so that the same person can't vote again
        print("-----------------------------------")
        print("To give vote to", nominee1,"Press 1")
        print("To give vote to", nominee2,"Press 2")
        print("-----------------------------------")
        vote = int(input("Enter your precious vote: "))
        if vote == 1:
            nm1_votes += 1
            print(nominee1,"Thank you for your vote")
        elif vote == 2:
            nm2_votes += 1
            print(nominee2, "Thank you for your vote")
        elif vote > 2:
            print("Invalid Choice")
        else:
            print("You are not eligible to vote OR have already voted")
